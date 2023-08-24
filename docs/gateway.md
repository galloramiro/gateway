# Gateway


## What is a gateway
It's gonna be the class that would manage all the logic and interactions with a 3rd party service.
Ideally this should:
- Receive the less amount of parameters as possible
- Return a base python object (list, dict, int, bool, etc) or a pydantic model if we want
- Abstract all the logic that belong to the services, as log in, getting tokens, etc
- Have contract testing


## What are the advantages of using a gateway to interact with 3rd party services 
If you manage to fulfill all, or of some of the points up there you would be able to enjoy some of the following things:
- Group logic to interact with the service
- Clear separation of the business logic to this 3rd party service interaction logic
- Capacity to be moved into another project quickly and without pain
- Capacity to transform this into a package
- Be easily replace in case of needed
- Maintainable with only 2 files, the class file and the contract test file
- Easy to mock 
- Secrets and env variables in only one place
- One place, and one way of logging the interaction
- Move all the calls from sync to async? change the base gateway and some little things and its solved 
- Specific error handling 


## What are the disadvantages of not using it to interact with 3rd party services
- Lonely functions in different places and in utils files
- Mix business logic with service interaction logic
- Not easy to move
- Variables and code repeated
- Move all calls from sync to async? find all the usage of request and be prepared to get your hands dirty 
- Lovely to maintain


## How this is looks like?
- [BaseGateway](https://github.com/galloramiro/gateway/blob/main/src/base_gateway.py)
- [ServiceGateway](https://github.com/galloramiro/gateway/blob/main/src/alpha_vantage_gateway.py)


## Did I say contract testing earlier? 
Yes, this is the last thought that I want to share, and its around how to test this.
And my approach would be the following:
- Mock the expected responses on the places where this is a dependency
- Mock the responses to test all the error handling that you could have
- Use contract testing to test that the values that you need are still being return on the service
  - would help you notice any not inform change
  - would help you know where the error is without going through the logs
- [Quick example of how a contract test would look like](https://github.com/galloramiro/gateway/blob/main/tests/test_alpha_vantage_gateway.py)