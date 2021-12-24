# Создание проекта ###
								     
	composer create-project laravel/laravel example-app		     
					     	
	composer global require laravel/installer			     
	laravel new example-app						     
								     	
## Крайний случай 					     
	composer create-project --prefer-dist laravel/laravel example-app    
	composer update --ignore-platform-reqs				     
--------------------------------------------------


# Запуск сервера #
	php artisan serve            



## Создание контроллера 
	php artisan make:controller ProductController 		    
	php artisan make:controller ProductController --api         
	php artisan make:controller PhotoController --resource	    	


## Создание модели
	php artisan make:model Product		      
	php artisan make:model Product --migration	     
--------------------------------------------- 

## Миграции  

### Создать миграцию           
									
    php artisan make:migration create_users_table --create=users
**** create_users_table - класс миграции; users - название таблицы в бд
### Редактировать миграцию 
	php artisan make:migration add_votes_to_users_table --table=users
-----------------------------------------------------------



# Запуск всех необходимых вам миграций 
 
    php artisan migrate
    php artisan migrate:refresh
    php artisan migrate:fresh --seed
-------------------------------------------------





# Создание seeders 
					 
	php artisan make:seeder ExampleSeeder    
	php artisan make:factory ExampleFactory  
					 




# Создание формы валидации 
    
    php artisan make:request UpdateUserRequest



# Очистить кеш после изменения .env 
        
    php artisan cache:clear



