<?php

        ### SORTING ###
        $arr = [12, 3, 8, 2, 4, 7];

        $arr[] = 3; # Push element in array

        sort($arr);  # sorting
        rsort($arr); # reverse sorting 
    
        $arr = ['g' => 'gamma', 'a' => 'alpha', 'b' => 'bravo'];
    
        asort($arr); # sorting of values
        ksort($arr); # sorting keys

        /* functions to print array */
        var_dump($arr); 
        print_r($arr);  
        