# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ...core.serialization import FieldMetadata
from .versions_get_response_edition import VersionsGetResponseEdition
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class VersionsGetResponse(UniversalBaseModel):
    release: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current release version of Label Studio
    """

    label_studio_os_package: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="label-studio-os-package")
    ] = pydantic.Field(default=None)
    """
    Information about the Label Studio open source package
    """

    label_studio_os_backend: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="label-studio-os-backend")
    ] = pydantic.Field(default=None)
    """
    Information about the Label Studio backend
    """

    label_studio_frontend: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="label-studio-frontend")
    ] = pydantic.Field(default=None)
    """
    Information about the Label Studio frontend
    """

    dm2: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Information about the Data Manager 2.0 component
    """

    label_studio_converter: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]], FieldMetadata(alias="label-studio-converter")
    ] = pydantic.Field(default=None)
    """
    Information about the Label Studio converter component
    """

    edition: typing.Optional[VersionsGetResponseEdition] = pydantic.Field(default=None)
    """
    Label Studio edition (Community or Enterprise)
    """

    lsf: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Information about the Label Studio Frontend library
    """

    backend: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Additional backend information
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
