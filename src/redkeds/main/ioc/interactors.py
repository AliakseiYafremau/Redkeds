from dishka import Provider, Scope, provide

from redkeds.application.interactors.chat.create import CreateChatInteractor
from redkeds.application.interactors.chat.delete import DeleteChatInteractor
from redkeds.application.interactors.chat.messages.delete import (
    DeleteChatMessageInteractor,
)
from redkeds.application.interactors.chat.messages.read import ReadMessageInteractor
from redkeds.application.interactors.chat.messages.send import SendChatMessageInteractor
from redkeds.application.interactors.chat.read import ReadUserChatInteractor
from redkeds.application.interactors.city.read import ReadCitiesInteractor
from redkeds.application.interactors.communication_method.read import (
    ReadCommunicationMethodsInteractor,
)
from redkeds.application.interactors.file.read import ReadFileInteractor
from redkeds.application.interactors.like.add_like import AddLikeInteractor
from redkeds.application.interactors.like.delete_like import DeleteLikeInteractor
from redkeds.application.interactors.recommendation_feed.read import (
    ReadRecommendationFeed,
)
from redkeds.application.interactors.skip.add_skip import AddSkipInteractor
from redkeds.application.interactors.skip.delete_skip import DeleteSkipInteractor
from redkeds.application.interactors.specialization.read import (
    ReadSpecializationsInteractor,
)
from redkeds.application.interactors.tag.read import ReadTagsInteractor
from redkeds.application.interactors.user.auth import AuthUserInteractor
from redkeds.application.interactors.user.default_photo.read import (
    ReadDefaultPhotoInteractor,
)
from redkeds.application.interactors.user.delete import DeleteUserInteractor
from redkeds.application.interactors.user.read import ReadUserInteractor
from redkeds.application.interactors.user.register import RegisterUserInteractor
from redkeds.application.interactors.user.update import UpdateUserInteractor
from redkeds.application.interactors.work.create import CreateWorkInteractor
from redkeds.application.interactors.work.delete import DeleteWorkInteractor
from redkeds.application.interactors.work.read import (
    ReadAllWorksInteractor,
    ReadWorkInteractor,
)
from redkeds.application.interactors.work.update import UpdateWorkInteractor


class InteractorsProvider(Provider):
    register_user_interactor = provide(
        RegisterUserInteractor,
        scope=Scope.REQUEST,
    )
    auth_user_interactor = provide(
        AuthUserInteractor,
        scope=Scope.REQUEST,
    )
    read_user_interactor = provide(
        ReadUserInteractor,
        scope=Scope.REQUEST,
    )
    update_user_interactor = provide(
        UpdateUserInteractor,
        scope=Scope.REQUEST,
    )
    delete_user_interactor = provide(
        DeleteUserInteractor,
        scope=Scope.REQUEST,
    )
    read_default_photo_interactor = provide(
        ReadDefaultPhotoInteractor,
        scope=Scope.REQUEST,
    )
    read_tag_interactor = provide(
        ReadTagsInteractor,
        scope=Scope.REQUEST,
    )
    read_communication_method_interactor = provide(
        ReadCommunicationMethodsInteractor,
        scope=Scope.REQUEST,
    )
    read_specializations_interactor = provide(
        ReadSpecializationsInteractor,
        scope=Scope.REQUEST,
    )
    read_cities_interactor = provide(
        ReadCitiesInteractor,
        scope=Scope.REQUEST,
    )
    read_work_interactor = provide(
        ReadWorkInteractor,
        scope=Scope.REQUEST,
    )
    read_all_works_interactor = provide(
        ReadAllWorksInteractor,
        scope=Scope.REQUEST,
    )
    create_work_interactor = provide(
        CreateWorkInteractor,
        scope=Scope.REQUEST,
    )
    update_work_interactor = provide(
        UpdateWorkInteractor,
        scope=Scope.REQUEST,
    )
    delete_work_interactor = provide(
        DeleteWorkInteractor,
        scope=Scope.REQUEST,
    )
    read_feed_interactor = provide(
        ReadRecommendationFeed,
        scope=Scope.REQUEST,
    )
    chat_create_interactor = provide(
        CreateChatInteractor,
        scope=Scope.REQUEST,
    )
    chat_delete_interactor = provide(
        DeleteChatInteractor,
        scope=Scope.REQUEST,
    )
    chat_read_interactor = provide(
        ReadUserChatInteractor,
        scope=Scope.REQUEST,
    )
    chat_message_delete_interactor = provide(
        DeleteChatMessageInteractor,
        scope=Scope.REQUEST,
    )
    chat_message_read_interactor = provide(
        ReadMessageInteractor,
        scope=Scope.REQUEST,
    )
    chat_message_send_interactor = provide(
        SendChatMessageInteractor,
        scope=Scope.REQUEST,
    )
    file_interactor = provide(
        ReadFileInteractor,
        scope=Scope.REQUEST,
    )
    add_like_interactor = provide(
        AddLikeInteractor,
        scope=Scope.REQUEST,
    )
    delete_like_interactor = provide(
        DeleteLikeInteractor,
        scope=Scope.REQUEST,
    )
    add_skip_interactor = provide(
        AddSkipInteractor,
        scope=Scope.REQUEST,
    )
    delete_skip_interactor = provide(
        DeleteSkipInteractor,
        scope=Scope.REQUEST,
    )
