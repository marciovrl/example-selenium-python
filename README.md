# example-selenium-python [![CircleCI](https://circleci.com/gh/marciovrl/example-selenium-python.svg?style=svg)](https://circleci.com/gh/marciovrl/example-selenium-python)
Example UI testing using Selenium with Behave in Python.

# Run project
- Clone project
```
git clone https://github.com/marciovrl/example-selenium-python.git
```

# Run in a Docker
- Build conteiner
```
docker build -t docker-behave .
```

- Run conteiner
```
docker run docker-behave
```

# Run without Docker use 
- Install dependencies
```
pip install -r requirements.txt
```

- Run test
```
behave features/specifications/search_item.feature
```