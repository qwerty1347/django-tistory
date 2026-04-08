from pathlib import Path


def ensure_directory(dir_path: Path) -> None:
    """
    지정된 경로 디렉토리가 존재하지 않으면 디렉토리를 생성합니다.

    Args:
        dir_path (Path): 디렉터리 경로.
    """
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)