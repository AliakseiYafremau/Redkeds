#!/usr/bin/env python3
import argparse
import os
import sys
import uuid

import psycopg2
from psycopg2.extras import RealDictCursor


def parse_args():
    p = argparse.ArgumentParser(
        description="Сохранить фото в файлы, названные UUID из users.photo и works.<column>."
    )
    # Параметры БД
    p.add_argument("--db-host", required=True)
    p.add_argument("--db-port", default="5432")
    p.add_argument("--db-name", required=True)
    p.add_argument("--db-user", required=True)
    p.add_argument("--db-password", required=True)

    # Таблицы/поля (можно менять при вызове)
    p.add_argument("--users-table", default="users")
    p.add_argument("--users-photo-column", default="photo")
    p.add_argument("--works-table", default="works")
    p.add_argument("--works-uuid-column", default="file_path")

    # Файлы/папки
    p.add_argument("--photo", required=True, help="Путь к исходной фотографии")
    p.add_argument("--outdir", required=True, help="Папка, куда писать файлы")
    p.add_argument(
        "--overwrite",
        action="store_true",
        help="Разрешить перезапись существующих файлов",
    )

    return p.parse_args()


def validate_uuid(s: str) -> str:
    try:
        return str(uuid.UUID(s))
    except Exception:
        return ""


def fetch_uuids(conn, users_table, users_photo_col, works_table, works_uuid_col):
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        # users.photo
        cur.execute(
            f"""
            SELECT DISTINCT {users_photo_col} AS u
            FROM {users_table}
            WHERE {users_photo_col} IS NOT NULL
            """
        )
        users_vals = [r["u"] for r in cur.fetchall()]

        # works.<uuid_column>
        cur.execute(
            f"""
            SELECT DISTINCT {works_uuid_col} AS u
            FROM {works_table}
            WHERE {works_uuid_col} IS NOT NULL
            """
        )
        works_vals = [r["u"] for r in cur.fetchall()]

    # Валидация UUID и объединение
    all_raw = [str(x) for x in (users_vals + works_vals)]
    valid = set()
    invalid = []
    for s in all_raw:
        v = validate_uuid(s)
        if v:
            valid.add(v)
        else:
            invalid.append(s)
    return sorted(valid), invalid


def main():
    args = parse_args()

    # Проверим исходную фотку
    if not os.path.isfile(args.photo):
        print(f"Ошибка: файл не найден: {args.photo}", file=sys.stderr)
        sys.exit(1)
    with open(args.photo, "rb") as f:
        photo_bytes = f.read()
    if not photo_bytes:
        print("Ошибка: исходная фотография пустая или не читается.", file=sys.stderr)
        sys.exit(1)

    # Папка назначения
    os.makedirs(args.outdir, exist_ok=True)

    # Подключение к БД
    try:
        conn = psycopg2.connect(
            host=args.db_host,
            port=args.db_port,
            dbname=args.db_name,
            user=args.db_user,
            password=args.db_password,
        )
    except Exception as e:
        print(f"Не удалось подключиться к БД: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        uuids, invalid = fetch_uuids(
            conn,
            args.users_table,
            args.users_photo_column,
            args.works_table,
            args.works_uuid_column,
        )
    finally:
        conn.close()

    if invalid:
        print(
            f"Предупреждение: пропущено не-UUID значений: {len(invalid)}",
            file=sys.stderr,
        )

    if not uuids:
        print("UUID не найдены. Нечего сохранять.")
        return

    # Запись файлов
    written = 0
    skipped = 0
    for u in uuids:
        out_path = os.path.join(args.outdir, u)
        if os.path.exists(out_path) and not args.overwrite:
            skipped += 1
            continue
        try:
            with open(out_path, "wb") as wf:
                wf.write(photo_bytes)
            written += 1
        except Exception as e:
            print(f"Ошибка записи {out_path}: {e}", file=sys.stderr)

    print(
        f"Готово. Всего UUID: {len(uuids)} | записано: {written} | пропущено (существуют): {skipped}"
    )
    if invalid:
        print(f"Также пропущено невалидных значений: {len(invalid)}")


if __name__ == "__main__":
    main()
