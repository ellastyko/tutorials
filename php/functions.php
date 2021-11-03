<?php

        ### SORTING ###
    $arr = [12, 3, 8, 2, 4, 7];

    sort($arr);  # sorting
    rsort($arr); # reverse sorting 

    $arr = ['g' => 'gamma', 'a' => 'alpha', 'b' => 'bravo'];

    asort($arr); # sorting of values
    ksort($arr); # sorting keys

    var_dump($arr); # print array
