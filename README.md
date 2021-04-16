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
