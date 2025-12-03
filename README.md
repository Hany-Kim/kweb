# kweb 2.0.4

KLayout Web Viewer ![demo](docs/_static/kweb.png)

Based on https://github.com/klayoutmatthias/canvas2canvas

## Install & Run

### Through uv

python uv로 다음을 실행합니다:

```bash
export KWEB_FILESLOCATION="/path/to/gds/folder" # or the windows equivalent with set
cd src/kweb
uv run default.py
```

#### Advanced Usage

KWeb은 두 가지 기본 앱을 제공합니다.

브라우저:

폴더의 파일 브라우저와 해당 폴더의 gds 파일을 볼 수 있는 kweb 뷰어를 제공하는 버전입니다. 함수를 가져오고 env 변수를 kweb.browser.get_app설정하여 함수에 전달할 수 있습니다. 또는 env 변수만 찾는 기본 버전도 있습니다.KWEB_FILESLOCATIONfileslocation=<Path object for target folder>kweb.default.app

뷰어:

엔드포인트 만 활성화하고 /gds/<filename>루트 경로, 즉 파일 브라우저는 활성화하지 않습니다. 에서 사용할 수 있습니다 kweb.viewer.get_app. 이 버전은 env 변수에 대한 리스너를 제공하지 않습니다. fileslocation대신 함수의 매개변수를 사용하세요.

### Development

#### Clone & Install

```bash
# Clone the repository to your local
git clone https://github.com/gdsfactory/kweb.git
```

#### Set a folder for kweb to use when looking for gds files

```bash
export KWEB_FILESLOCATION=/path/to/folder/with/gdsfiles
```

#### Run

```bash
cd src/kweb
uv run default.py
```

Copy the link http://127.0.0.1:8765/gds/file.gds (or http://localhost:8765/gds/file.gds also works) to your browser to open the waveguide example
