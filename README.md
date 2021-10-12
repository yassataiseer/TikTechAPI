# TikTechAPI
## API backend for TikTech LLC.

### Basic Code Structure

| Blueprints | Purpose |
| ------ | ------ |
| Users | Manage all possible users |
| Clients | Manage all possible customer data |
| Services | Manage all possible services that the client can access |
| Inventory | Manage all inventory @tiktech store |



### Testing:
Testing is directly proportionate to the work done. View under `tests` directory and to execute simply run:
`python -m pytest`. 

### Testing Requirements:
Testing works very easily within this API. Make sure to not be using any
docker containers or closed environments that prevent access to the MySQL db.

### Virutual ENV:
``` 
python3 -m venv env
source env/bin/activate
deactivate
^to deactivate env
```