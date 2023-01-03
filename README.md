## TODO


    scrap for a data:
        - get x_rays images for healthy lungs and with illness
        - prepare labaled directories
        - ~split directiories into: train, val, test sets~
    *NEW* get the data:
        - since getting a nice and useful dataset from scrappin might be too much time consuming
        i will use already prepared kaggle's x_ray dataset
    plot the data:
        - confront healthy lungs with an ill one
    preprocess the data:
        - openCV:
            - what to do with this lib
            - how to preprocess images
            - can we save preprocessed images
            - does it have any data augmenations
            - for data augmentation i will oversample dataset
            - which preprocessing techniques are most viables and why, what does each of them is for
    build a model class:
        - init neural network model:
            - Since its image recognition task i will build CNN
            - build NN
        - perform training:
            1. get prediction
            2. compare it with actuall label
            3. optimize weights (not weights for labels)
            4. log results with proper /*metric*/:
                - which metric should i focus on and what are the main difference
                - As far as training dataset is conserned i will use accuracy since i will oversample that each class (Pneumonia/Normal) will have the same number of sample, but for validation i will use precision/recall to get info how many Positive labels are really true.
        - perform validatiion:
            steps are the same BUT we are not optimizing weights - we dont want to change weights durign validation process
        - callback:
            i want training to stop if it doesnt have any result after aprox ~ 5 epochs
        - logging:
            as mentioned I want to have everything logged:
                - trainingng process
                - validatiion process
                to see wheteher there is overfittin/underfitting
                And i want to have a clear comparison of metrics -> it will be used to determin quality of
                chosen models
    Perform training/validating
    Count how many predictions are ok and how many were wrong:
        - why they were wrong, plot images maybe to justify what they have incommon which influenced the results
    Mby here some statistics comparison for each models?
    
##  AFTER THIS:

    Testing?
    API:
        - i can create an API which will have prob one endpoint which accepts an Image of an x_ray to classify it
        as healthyy or not:
            * uploaded image will be preprocessed!
        - it should work asynchronously!
        - I want have celery workes so app will handle many executions
        - Database would be also nice to store uploaded image -> add it to the training data so it can become bigger
        - cover api with testing
        - cover api with handling such things like:
            - not a x_ray image
            - not a chest_x_ray image
            - bad quality of an image
    Contenerization:
        put everything into a docker
           
