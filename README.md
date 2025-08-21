# Aviability Checker 

I used fastApi and requests. The whole project is made in a virtual environment and with the following main packages:

| package  | version  | 
|----------|----------|
| fastapi  | 0.116.1  |  
| requests | 2.32.4   | 


## API Reference

#### Checker aviability

```http
  POST /check
    {
        "links": [array]
    }
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `array[string]` | **Required**. links |

```
answer:{
  "request": {
    "link": {
      "available": bool,
      "code": int,
      "info": str
    }
  }
}
```

#### Start page

```http
  GET /
```

```
answer:{
  "request": {
    "link": {
      "available": bool,
      "code": int,
      "info": str
    }
  }
}
```
## Run Locally

Clone the project

```bash
  git clone https://github.com/LiksLaur/AviabilityCheckerAPI/tree/main
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install requests fastapi[all]
```

Start the server

```bash
  uvicorn app.main:app --reload  
```

