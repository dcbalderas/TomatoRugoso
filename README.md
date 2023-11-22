# TomatoeRugoso: A Multiclass Tomatoe Rugoso Image Dataset for Deep Learning

This repository makes available the source code and public dataset for the work, "TomatoRugoso: Tomato brown fruit virus, an open-access Tomatoes Rugoso’s dataset for computer visual inspection", published with open access by Scientific Reports: https://www.. The TomatoRugoso dataset consists of 242 images capturing eight different parts of the tomato plant infected with rugoso. In our work, the dataset was classified to an average accuracy of TODO:... without and 40% with Data Augmentation the Yolo7 deep convolutional neural network.

The source code, images and annotations are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. The contents of this repository are released under an [Apache 2](LICENSE) license.

## Images Sources
The TomatoRugoso repository contains a collection of photographs of tomatoe plant infected with rugoso which can be used to train a image classifiers or be used in machine learning projects. A variety of categories have been provided to ensure a diverse selection of images for the best and most accurate results.

These images were taken from different setup environment using the following rules:
1.

## Stats
There are **242** across **8** clases.

Class | Type of plant | Part of the plant | Current Plant Condition | Label | Number of labels 
------ | ------ | ------ | ------ | ------ | ------ 
| ------ | --------- |
1   | Tomato    | Leaf  | Healthy   | T_L_H     | 100 
2   | Tomato    | Leaf  | Rugoso    | T_L_R     | 100 
3   | Tomato    | Steam | Healthy   | T_S_H     | 100 
4   | Tomato    | Steam | Rugoso    | T_S_R     | 100 
5   | Tomato    | Flower| Healthy   | T_Fl_H    | 100 
6   | Tomato    | Flower| Rugoso    | T_Fl_R    | 100 
7   | Tomato    | Fruit | Healthy   | T_F_H     | 100 
8   | Tomato    | Fruit | Rugoso    | T_F_R     | 100 

TODO:... all          48         699        0.33       0.266       0.213       0.143

## Data organization

Images are assigned unique filenames with increasing ID number. The images were photographed either directly in a laboratory or directly on the field. The format is like so: ```xxxxx.jpg```, where the ID is simply an integer from 0 to the current number of image.

## Images labeling

The images are placed in a single train folder using the Pascal VOC (Visual Object Classes) folder format.

* Original Images without labels
** Resize to 1280x1280 (Stretch)
** Resize to 640x640 (Stretch)
** Resize to 416x416 (Stretch)

The labels.xml file assigns species labels to each image. It is a comma separated text file in the Pascal VOC (Visual Object Classes) format. Example:

```
<annotation>
    <folder></folder>
    <filename>000001.jpg</filename>
    <path>000001.jpg</path>
    <source>
        <database>tomate_rugoso</database>
    </source>
    <size>
        <width>500</width>
        <height>375</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
    <object>
        <name>helmet</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <occluded>0</occluded>
        <bndbox>
            <xmin>179</xmin>
            <xmax>231</xmax>
            <ymin>85</ymin>
            <ymax>144</ymax>
        </bndbox>
    </object>
    <object>
        <name>helmet</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <occluded>0</occluded>
        <bndbox>
            <xmin>112</xmin>
            <xmax>135</xmax>
            <ymin>145</ymin>
            <ymax>175</ymax>
        </bndbox>
    </object>
</annotation>
```

## Training

### First Model
TODO:...

### Second Model
To train the second model Data Augmentation was applied, the following processing were performed to the images: 

* No transformation
* Vertical flip
* Horizontal flip
* Horizontal and vertical flip
* Rotations 90° and 180°
* Crops pixels at the sides of the image - percentage 0.8
* Resizes the image - percentage" : 0.9, method:"INTER_NEAREST
* Translation: Translates the image- x: 10, y: 10})

The transformation lead to 2,178 images which were splitted in 70-10-20, resulting in training 1,524, testing 219 and validation 435 images.

## Download the dataset images and our trained models

## models

We provide the most successful YoloV7 models saved in TODO:...Keras' hdf5 model format. 
```
TODO:... .hsmlsdrt
```

## BibTeX (TODO: Update)
```
@article{TomatoRugoso2024,
  author = {David Balderas-Silva and
    Pedro Ponce Cruz and 
    Arturo Molina},
  title = {{TomatoRugoso: Tomato brown fruit virus, an open-access Tomatoes Rugoso’s dataset for computer visual inspection}},
  journal = {TODO:...},
  year = 2024,
  number = TODO:...,
  month = TODO:...,
  volume = TODO:...,
  issue = TODO:...,
  day = TODO:...,
  url = "https://doi.org/TODO:...",
  doi = "TODO:..."
}

```
