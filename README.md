# GEOG5003 - Assignment 2
This is a Cellular Model used to simulate a site suitability analysis process to identify possible suitable location for constructing a factory that makes rock aggregate somewhere in the UK.

The Model Design Process include:

> 1)	Creteria Selection # Geology, Transport and Population
> 2)	Layer Normalization # Setting datasets to the same scale e.g. 0 to 255.
> 3)	Weighted Overlay # Combining the three layers

The model takes in data from a web-page containing x, y and z values to create the agents for this model. Additionally, the model also reads data from an external file containing a 2D list simulating an enviroment. This enviroment represents 2D space where the agents can interact with other agents and other elements in that space. In this model, agents can move freely, "eat", modify and share their resources with other agents provided that they are within the neighborhood.

The model, when successfully executed, results into a Graphical User Interface showing the agents interaction based on a certain number of agents and iterations.

__Project Structure:__

> * Agent Framework.py  - this is agent class which defines the agents behaviours through move, eat and share data methods.
> * Model.py - defines the model  and  its functions for executing different components of the model.
> * .gitattributes - gives attributes to pathnames in the model.
> * Capture.PNG - A sample screenshot of an animated canvas resulting from the agents interactions.
> * LICENSE - repository license permiting open source capablities for its use, change and distribution by other users
> * README.md - description of project structure and functionality
> * environment.output.txt - a 2D list respresenting the agents interaction space
> * in.txt - contains raster data with values equivalent to image pixels
> * pycache - a directory automatically generated by python that contains cache files

__Running the Model:__

To run the model, execute model.py from console. Once the file has loaded, enter the values of the number of agents, the number of iterations and the number of Neighbour’s.

Once the model has been executed, it will display a GUI. From the __File__ menu, click __Run Model__.
This will display an animated canvas as shown below.