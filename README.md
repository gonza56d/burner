# Burner

## Requirements

- Implement unittest using the *coverage* library
- Use virtual env
- Use a file for external installations

## Challenge 1: Collecting data

We want to create a historical website, in order to help
to the people tracking the price evolution of a product.

Lets create an script which collect from several webpages
(Falabella and Sodimac):

- Store name
- Product ID
- Product name
- Product category
- Price

Create a CSV file for every store with the previous values.

### Hints

You can use the **bs4** module.

### Goal

Run the script in a docker container every day.


# How to run

## Using manger

In order to run our scrapper application, we have to execute commands
from the manager (manage.py) like this:

`$ python3 manage.py --pages='$PAGE_1 $PAGE_2' --tasks='$TASK_1 $TASK_2 $TASK_3 $TASK_N'`

And each task will be executed (in order) for every page.<br>

For example:

`$ python3 manage.py --pages='falabella sodimac' --tasks='collectcategories collectproducts'`

So that we will first scrap categories, and then products, from both Falabella and Sodimac.<br>

### Available pages:

* falabella
* sodimac

### Available tasks:

* collectcategories
* collectproducts
