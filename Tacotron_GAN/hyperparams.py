# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/tacotron
'''

class Hyperparams:
    '''Hyper parameters'''
    # mode
    sanity_check = False
    gan_mode = True
    
    # data
    #text_file = 'WEB/text.csv'
    #sound_fpath = 'WEB'
    data_path = 'data/'
    fpath = '../data/female_us/'
    mpath = '../data/male_us/'
    # fpath = '../../cmu_artic/female_us_slt/'# desktop
    # mpath = '../../cmu_artic/male_us_bdl/'# desktop

    bin_size_x = (1,2)
    bin_size_y = (1,2)

    max_len = 48 #unsure about what this is used for
    # max_len = 100 if not sanity_check else 30 # maximum length of text
    # min_len = 10 if not sanity_check else 20 # minimum length of text
    
    # signal processing
    #sr = 22050 # Sampling rate. Paper => 24000
    sr = 16000
    n_fft = 1024#2048 # fft points (samples)
    frame_shift = 0.0125 # seconds
    frame_length = 0.05 # seconds
    hop_length = int(sr*frame_shift) # samples  This is dependent on the frame_shift.
    win_length = int(sr*frame_length) # samples This is dependent on the frame_length.
    n_mels = 80 # Number of Mel banks to generate
    power = 1.2 # Exponent for amplifying the predicted magnitude
    n_iter = 30 # Number of inversion iterations 
    use_log_magnitude = True # if False, use magnitude
    
    # model
    #embed_size = 256 # alias = E
    embed_size = n_fft/2 #n_mels
    encoder_num_banks = 10 # Paper => 16
    decoder_num_banks = 8
    num_highwaynet_blocks = 2
    r = 5 # Reduction factor. Paper => 2, 3, 5
    norm_type = 'ins'  # a normalizer function. value: bn, ln, ins, or None
    
    # training scheme
    k = 5 # number of times to train the generator for each discriminator train
    lr = 0.001 # Paper => Exponential decay
    logdir =  "logdir_s" if  sanity_check  else "logdir_gan" if gan_mode else "logdir"
    outputdir = "samples_s" if  sanity_check else "samples_gan" if gan_mode else "samples"
    batch_size = 32
    num_epochs = 10000 if not sanity_check else 40 # Paper => 2M global steps!
    loss_type = "l1" # Or you can test "l2"
    num_samples = 32

    # summary scheme
    audio_summary = 100 #number of epochs until next sample
    
    # etc
    num_gpus = 2 # If you have multiple gpus, adjust this option, and increase the batch size
                 # and run `train_multiple_gpus.py` instead of `train.py`.
    target_zeros_masking = False # If True, we mask zero padding on the target, 
                                 # so exclude them from the loss calculation.     
