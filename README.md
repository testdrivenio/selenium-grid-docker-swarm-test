# Distributed Testing with Selenium Grid and Docker

Distribute automated tests with Selenium Grid and Docker Swarm

## Want to use this project?

1. Fork/Clone

1. Create and activate a virtualenv

1. Install the requirements

1. [Sign up](https://m.do.co/c/d8f211a4b4c2) for Digital Ocean and [generate](https://www.digitalocean.com/community/tutorials/how-to-use-the-digitalocean-api-v2) an access token

1. Add the token to your environment:

    ```sh
    $ export DIGITAL_OCEAN_ACCESS_TOKEN=[your_token]
    ```

1. Spin up five droplets and deploy Docker Swarm:

    ```sh
    $ sh project/create.sh
    ```

1. Set the environment variable:

    ```sh
    $ eval $(docker-machine env node-1)
    $ NODE=$(docker service ps --format "{{.Node}}" selenium_hub)
    $ export NODE_HUB_ADDRESS=$(docker-machine ip $NODE)
    ```

1. Run the tests:

    ```sh
    $ python project/parallel_test_run.py
    ```

1. Bring down the resources:

    ```sh
    $ sh project/destroy.sh
    ```
