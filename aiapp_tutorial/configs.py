from pydantic_config import SettingsConfig, SettingsModel


class AppConfig(SettingsModel):
    infer_model_name_or_path: str = 'mobilenetv4_conv_small.e2400_r224_in1k'

    model_config = SettingsConfig(
        env_file='.env',
        case_sensitive=False
    )


cfg = AppConfig()
