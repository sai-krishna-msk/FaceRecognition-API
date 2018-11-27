For producing training data in the form of pickle you just need to run
```
python pickle_dataset.py
```
and you would be asked for how many people you want to train and names respectively by providing that information, and looking into the camera
of your device, at slightly different angles it would generate total 25 images each(person)

You could then suitable upload this pickle file at suggested end point and your model is trained

If you want to manually update the dataset of people you can do that and run
```
python exsistingImages_pickle.py
```
