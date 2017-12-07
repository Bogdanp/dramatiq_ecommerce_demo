# dramatiq_ecommerce_example

This is an example Django app I built for a talk I gave at the
RoPython-Cluj user group.  You can find the slides [here][slides].


## Setup

1. Clone the repo, then run `pipenv install`.
1. Run [RabbitMQ].
1. Provision the database with: `./scripts/provision.sh`
1. Run the web server: `python manage.py runserver`
1. Run the workers: `python manage.py rundramatiq`

## License

django_dramatiq_example is licensed under Apache 2.0.  Please see
[LICENSE][license] for licensing details.


[slides]: https://slides.com/bogdanpopa/dramatiq/
[license]: https://github.com/Bogdanp/dramatiq_ecommerce_example/blob/master/LICENSE
[RabbitMQ]: https://rabbitmq.com
