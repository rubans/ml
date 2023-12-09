# Overview
Provided Jupyter Notebook (cifar_pipeline_creator.ipynb) will create (compile & deploy) a Vertex AI pipeline to do the following:
    1. Trains the model provided.
    2. Uploads the trained model to Vertex AI as a model resource.
    3. Deploys the model resource to the an endpoint resource.
       
Include model changes to do the following:
    1. Update the model specification to include an additional convolutional layer containing 16 filters with a kernel size of 3.
    2. Add a max pooling layer after each of the convolutional layers to reduce the dimensionality of the outputs passed to the next layer.
    3. Add a callback to save a model checkpoint after every training epoch.
    
# Pre-requisites
    1. Used workbench instance : workbench-instances-v20230404-debian-11-py310 (M106)
    2. Ensure the default SA used to run has the required Storage Admin IAM roles.
 
