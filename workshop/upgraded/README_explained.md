## upgraded(복사본) 폴더 구조 설명


이 파일은 `workshop/legacy`의 내용을 그대로 복사하여 생성된 `workshop/upgraded` 디렉터리의 구조와 주요 파일에 대한 간단한 설명을 제공합니다.

루트 파일 및 목적

- `MANIFEST.in` : 패키지 배포용 파일 목록 정의
- `README.rst` : 프로젝트/패키지에 대한 설명(원본 문서)
- `distribute-0.6.10.tar.gz` : 배포용 tarball (바이너리/압축파일)
- `distribute_setup.py` : distribute 설치 스크립트
- `setup.py` : 패키지 설치/설정 스크립트

`docs/`
- `Makefile` : 문서 빌드용 Makefile
- `build/` : Sphinx로 빌드된 정적 문서들
  - `doctrees/` : Sphinx 중간 도구 출력
  - `html/` : 빌드된 HTML 문서와 정적 자원
    - `_sources/` : 페이지 원본 텍스트
    - `_static/` : CSS/JS/이미지 등 정적 자원(예: `file.png`, `jquery.js`) — 일부 파일은 바이너리(이미지)
    - HTML 파일들: `index.html`, `getting_started.html` 등
- `source/` : Sphinx 문서 원본(`.rst` 및 `conf.py`)

`guachi/` (파이썬 패키지)
- `__init__.py` : 패키지 초기화
- `config.py`, `database.py` : 주요 모듈 코드
- `tests/` : 패키지 테스트

`guachi.egg-info/` : 패키지 메타데이터 (PKG-INFO 등)

바이너리/비텍스트 파일 안내

- `distribute-0.6.10.tar.gz` : 압축된 tarball — 복원하려면 `tar -xzf` 사용
- `docs/build/html/_static/*.png` (예: `file.png`, `minus.png`, `plus.png`) : 이미지 파일(바이너리)

바이너리 무결성 해시 (SHA256)

- `distribute-0.6.10.tar.gz` : 3046d9d6d4acedf5a7e2aa73f6370a0f9bf1556faad2904523f16c0945847630
- `docs/build/html/_static/file.png` : 1834b8fc8c98c09f88cb2264011c3ef917fe651f2678721384c0aae346dfb062
- `docs/build/html/_static/minus.png` : 141ae2a6288687b83d817f7fc0daef577e43d1410871f2f9fd1ceff0af825faa
- `docs/build/html/_static/plus.png` : 55fcc0d9d9d52070dae60f646ec56c0dd111be1c13459b06470c7ff5b6f2fbf7

검증 노트

- 원본 `legacy`의 파일과 디렉터리를 보존하여 그대로 복사했습니다.
- 텍스트 파일들은 내용이 유지됩니다. 바이너리/압축 파일은 복사본으로 포함되어 있으나, 바이너리의 무결성은 필요시 검증하세요 (예: `sha256sum`).

다음 단계 제안

- 필요하면 이 복사본에서 현대화(예: Python 3 호환성, 의존성 업데이트, 테스트 실행)를 진행하세요.
- 원본과의 차이 확인을 위해 `diff -ru legacy upgraded`를 사용해 변경 사항을 검토할 수 있습니다.

생성 날짜: 2025-09-26
