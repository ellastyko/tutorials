<?php
    
    namespace classes;

    function hello() {
        return "hi!";
    }

    class Human {

        public $age; 

        public function __construct($age = 18)
        {
            $this->age = $age;
        }

        public function humanity() {
            return "I am a human!";
        }
    }

    class Child extends Human {

        public function __construct($name)
        {
            parent::__construct();
            echo parent::humanity();
        }
    }


    $obj = new Child('Vadik');
    echo $obj->age;