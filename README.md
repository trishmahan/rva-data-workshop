# RVA Data Workshop 2020 Intro to Data Engineering

This work was created as part of the RVA Data Summit Workshop 2020 session, "Introduction to Data Engineering."

It provides a tested, deployable REST microservice that returns a calculated value.

For information on how to work with the microservice, see specification.yaml.
## Getting Started


### Prerequisites

Please install Docker, Pip and Python3

On Mac:
```
brew install docker
brew install python3
```

### Installing


To run the service locally:

Install the requirements
```
pip install -r requirements.txt
```

Install an editable, local version of the package
```
pip install -e .
```

Run the service locally
```
python3 app.py
```

Build and run the service in a container
```
docker build -t rvadatasummit/intro .
docker run -d -p 5000:5000 rvadatasummit/intro 
```

## Running the tests

You can run the tests using the Python pytest module.

```
pytest
```


## Deployment

To deploy in the cloud, follow instructions for your cloud provider:
* [AWS](https://docs.docker.com/docker-for-aws/deploy/)
* [Azure](https://docs.docker.com/docker-for-azure/deploy/)
* [Google Cloud](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app)

## Built With

* [Python](https://www.python.org/) - Used to write the service
* [Flask](https://palletsprojects.com/p/flask/) - Used as the web framework
* [Docker](https://www.docker.com/) - Used to run the service in a container

## Contributing

If you'd like to contribute please create a feature branch and a pull request. For more information on 
contributing best practices, check out the excellent
[contributing guidelines](https://pandas.pydata.org/docs/development/contributing.html) provided by Pandas.

## Authors

* [**Jackie Goldschmidt**](https://github.com/jackie-goldschmidt) - *Initial work*

See also the list of 
[contributors](https://github.com/jackie-goldschmidt/RVADataEngineeringWorkshop/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License.

## Acknowledgments

* Thank you to PurpleBooth for the [README template](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)