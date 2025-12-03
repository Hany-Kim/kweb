from kweb.browser import get_app
import uvicorn

app = get_app()

def main():
    uvicorn.run(app="default:app", host="0.0.0.0", port=8765, reload=True)

if __name__ == "__main__":
    main()

