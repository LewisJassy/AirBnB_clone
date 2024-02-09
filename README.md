# AirBnB Clone

This is a simplified clone of the AirBnB website implemented in Python. It allows users to manage various objects such as users, states, cities, places, and more.


## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:

   ```bash
   cd AirBnB_clone
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the command-line interface:

   ```bash
   python console.py
   ```

2. You will enter the interactive prompt where you can execute commands to manage the objects.

3. Available commands:
   - `create`: Create a new object instance.
   - `show`: Show details of a specific object.
   - `destroy`: Delete an object.
   - `update`: Update the attributes of an object.
   - `all`: Show details of all objects.
   - `count`: Get the count of objects.
   - Additional commands specific to the implemented models.

4. Example usage:

   ```bash
   (hbnb) create User
   (hbnb) show User 12345
   (hbnb) update User 12345 name John
   ```

## Features

- Manage users, states, cities, places, and other objects.
- Create, retrieve, update, and delete objects.
- Data storage using JSON files.
- Interactive command-line interface.
- Integration with unit tests for testing the functionality.

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, please open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/new-feature`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

