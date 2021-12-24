<?php

    # How to run php script ...@device: php basics.php 

    
        #### DATA TYPES ####

    # There are 8 data types in PHP
    

    $str = "some text";  # string
    $int = 5;             # integer
    $double = 5.5;         # double / float
    $arr = [1, 3, 5];       # array
    $null = null;             # NULL
    $bool = true;              # boolean
    $obj = function () { };        #object
    $fp = fopen('./basics.php', 'r');  #resourse

    /*
        You can check data type using this function
                
                    gettype();
    */





            ### How to print text ###

    echo "Hello world!", "ddd";

    print "Hello again!";  # Can receive only one argument

    
    


            ### Conditions and cycles ###

    if (true) 
        echo "1";    
    elseif (false) 
        echo "2";
    else 
        echo "3";


    switch(1) {
        case 1: echo "1"; break;
        case 2: echo "2"; break;
        default: echo "default"; break;
    }

    do {

    } while(false);
    
    while(false) {

    }

    $arr = ['a' => 'alpha', 'b' => 'bravo'];

    
    foreach ($arr as $value => $key) 
        echo $value;
    




        ### Constants
    define('ABS' , 34);
    // echo ABS; # 34

