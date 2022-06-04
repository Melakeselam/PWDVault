from src.domain.Host import Host
from src.service.dtos.HostDto import HostDto


class HostDtoAdaptor:
    def __init__(self) -> None:
        pass

    def model_to_info_dto(host: Host) -> HostDto:
        return HostDto(
            host.name(),
            host.platform_id(), 
            host.category_name(), 
            host.address(),
            host.custom_pwd_retention_period_in_hours()
            )
    
    def model_to_credentials_dto(host: Host) -> HostDto:
        return HostDto(
            host.id(),
            host.name(),
            host.platform_id(), 
            host.category_name(), 
            host.credentials(), 
            host.address()
            )

    def model_to_dto(host: Host) -> HostDto:
        return HostDto(
            host.user_id(),
            host.id(),
            host.name(),
            host.platform_id(), 
            host.category_name(), 
            host.credentials(),
            host.address(),
            host.custom_pwd_retention_period_in_hours()
            )
    
    def dto_to_model(host_dto: HostDto) -> Host:
        return Host(
            host_dto.user_id(),
            host_dto.id(),
            host_dto.name(),
            host_dto.platform_id(), 
            host_dto.category_name(), 
            host_dto.credentials(),
            host_dto.address(),
            host_dto.custom_pwd_retention_period_in_hours()
            )