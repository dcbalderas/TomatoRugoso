# TomatoeRugoso: A Multiclass Tomatoe Rugoso Image Dataset for Deep Learning

This repository makes available the source code and public dataset for the work, "TomatoRugoso: Tomato brown fruit virus, an open-access Tomatoes Rugoso’s dataset for computer visual inspection", published with open access by Scientific Reports: https://www.. The TomatoRugoso dataset consists of 242 images capturing eight different parts of the tomato plant infected with rugoso. In our work, the dataset was classified to an average accuracy of TODO:... without and 45% with Data Augmentation the Yolo7 deep convolutional neural network.

The source code, images and annotations are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. The contents of this repository are released under an [Apache 2](LICENSE) license.

## Images Sources
The TomatoRugoso repository contains a collection of photographs of tomatoe plant infected with rugoso which can be used to train a image classifiers or be used in machine learning projects. A variety of categories have been provided to ensure a diverse selection of images for the best and most accurate results.

These images were taken from different setup environment using the following rules:
1. Rugoso infection fully visible
2. Natural light ilumination 

## Stats
There are **242** images that included **8** clases.

Class | Type of plant | Part of the plant | Current Plant Condition | Label 
------ | ------ | ------ | ------ | ------ | ------     
1   | Tomato    | Leaf  | Healthy   | T_L_H     
2   | Tomato    | Leaf  | Rugoso    | T_L_R      
3   | Tomato    | Steam | Healthy   | T_S_H     
4   | Tomato    | Steam | Rugoso    | T_S_R      
5   | Tomato    | Flower| Healthy   | T_Fl_H     
6   | Tomato    | Flower| Rugoso    | T_Fl_R     
7   | Tomato    | Fruit | Healthy   | T_F_H      
8   | Tomato    | Fruit | Rugoso    | T_F_R      

## Data organization

Images are assigned unique filenames with increasing ID number. The images were photographed either directly in a laboratory or directly on the field. The format is like so: ```xxxxx.jpg```, where the ID is simply an integer from 0 to the current number of image.

The images are placed in a single train folder using the Pascal VOC (Visual Object Classes) folder format.

* original - Original Images without labels
** labeled1280x1280 - Labeled images, Resized to 1280x1280 
** labeled416x416 - Labeled images, Resized Resize to 416x416 
** labeled640x640 - Labeled images, Resized Resize to 640x640 
** labeled640x640_augmented - Labeled images, Resized Resize to 640x640 with data augmentation

## Images labeling

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

## Models

We provide the most successful YoloV7 models saved in *.pt* model format. All the models provided were trained for **1,000** epochs with the following hyperparameters. 
```
lr0=0.01, lrf=0.1, momentum=0.937, weight_decay=0.0005, warmup_epochs=3.0, warmup_momentum=0.8, warmup_bias_lr=0.1, box=0.05, cls=0.3, cls_pw=1.0, obj=0.7, obj_pw=1.0, iou_t=0.2, anchor_t=4.0, fl_gamma=0.0, hsv_h=0.015, hsv_s=0.7, hsv_v=0.4, degrees=0.0, translate=0.2, scale=0.9, shear=0.0, perspective=0.0, flipud=0.0, fliplr=0.5, mosaic=1.0, mixup=0.15, copy_paste=0.0, paste_in=0.15, loss_ota=1
```

The models trained are: 

```
models/best_00.pt
models/best_01.pt
```

### First Model
The first model provided is the Yolov7 trained using the labeled640x640 folder. It consist of 242 images which were splitted in 70-10-20, resulting in training **169**, testing **25** and validation **48** images. The resulting number of labels where *2,052*
 all        | 2052
 ------ | ------
 T_L_H     | 237
 T_L_R     | 1434
 T_S_H     | 54
 T_S_R     | 158 
 T_Fl_H    | 21 
 T_Fl_R    | 18 
 T_F_H     | 33 
 T_F_R     | 97 

The resulting model was saved in models/best_00.pt

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

The first model provided is the Yolov7 trained using the labeled640x640_augmented folder. The Data Augmentation lead to **2,178** images which were splitted in 70-10-20, resulting in training **1,524**, testing **219** and validation **435** images.

The resulting model was saved in models/best_01.pt


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
