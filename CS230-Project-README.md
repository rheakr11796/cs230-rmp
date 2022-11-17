# CS230Project-RMP
Code files for CS230 Project.


This repository contains all the main files that we are using for our CS230 project on boosting the performance of noise separation models, to eventually aid in cough classification into COVID/non COVID. It currently contains the following directories and files: 

(1) Data Loaders 
(1.a) prepare_data.py - data loader for the WSJ02-mix dataset, the initial training set to the SepFormer model 
(1.b) prepare_coughvid_data.py - data loader for the COUGHVID dataset to be used on the SepFormer model 

(2) Code files 
(2.a) train.py - Original SepFormer model, with very minor modifications to ensure the model runs on our systems 
(2.b) train_new.py - New SepFormer model with our proposed changes to the loss function to incorporate contrastive loss 

(3) Functions
(3.a) si-snr.py - Original loss function for SepFormer, reporting SI-SNR loss 
(3.b) contrastive.py - Contrastive loss function, which is added to the loss in train_new.py 
