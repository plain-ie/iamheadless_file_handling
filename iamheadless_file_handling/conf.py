from .apps import IamheadlessFileHandlingConfig as AppConfig


class Settings:

    APP_NAME = AppConfig.name
    VAR_PREFIX = APP_NAME.upper()

    VAR_FILE_HANDLING_BACKEND_CLASS = f'{VAR_PREFIX}_FILE_HANDLING_BACKEND_CLASS'

    @property
    def FILE_HANDLING_BACKEND_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_FILE_HANDLING_BACKEND_CLASS,
            f'{self.APP_NAME}.file_handling.LocalFileUploadBackend'
        )

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
