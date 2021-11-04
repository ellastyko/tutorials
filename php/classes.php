<?php
    
    namespace classes;


    class Human {

        private $id;
        public $age; 
        protected $name;

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
        }

        public function __invoke()
        {
            echo "invoke";
        }

        public function rename($name) {
            $this->name = $name;
        }
    }


    $obj = new Child('Vadik');
    echo $obj->age;
    $obj->rename('Josh');
