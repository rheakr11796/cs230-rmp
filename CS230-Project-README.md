# CS230Project-RMP
Code files for CS230 Project.
Rhea Kumar, Melissa Weyant, Pura Peetathawatchai

This repository contains the files that we have been working with so far for our project. These primarily build on the Speechbrain github repository from Ravanelli et al, which contains the code for the SepFormer sound separation model that we are using for our background noise separation tasks. 

The main files that we updated and created are as follows: 

(1) recipes/WSJ0Mix/separation/train.py: Original training file for the SepFormer. The main changes were adding a few commands around file paths in order to fix any training bugs that we encountered. 

(2) recipes/WSJ0Mix/separation/hparams/sepformer.yaml: Hyperparameters file for our existing training task. The main changes involved changing the number of epochs to 20 in order to generate a baseline for the milestone. 

(3) recipes/WSJ0Mix/separation/train_new.py: New training file that contains our draft implementation of the updated objective function for SepFormer, which we plan to train our data on for our final project. 

(4) recipes/WSJ0Mix/separation/contrastive_loss.py: New loss function file that contains the formula for contrastive loss, or the L2 distance between the two encodings. This will be used in train_new.py alongside the original SepFormer loss function to retrain and hopefully enhance performance of the SepFormer model. 

(5) recipes/WSJ0Mix/prepare_data.py: Data loader for the WSJ0Mix and COUGHVID datasets. 

Additionally, speechbrain/nnet/loss/si_snr_loss.py contains the original loss function for SepFormer. 

Citations:
@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}


