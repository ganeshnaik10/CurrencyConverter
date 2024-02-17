# CurrencyConverterApp

This Python script creates a simple currency converter application using the Tkinter library for GUI development. It fetches currency exchange rates from an API and allows users to convert amounts from one currency to another. Here's a breakdown of its features:

GUI Development:

The application's GUI is created using Tkinter, with themed widgets (ttk) for a modern appearance.
It includes labels, comboboxes for selecting currencies, an entry field for entering the amount, a button for conversion, and a label to display the result.
Currency Conversion:

Users can select currencies from dropdown lists and enter an amount to convert.
Upon clicking the "Convert" button, the application fetches the latest exchange rates from an API and performs the currency conversion.
The result is displayed in the GUI.
Background Thread:

A separate thread periodically updates the exchange rates in the background to ensure the rates are up to date.
This background thread runs continuously while the application is open.
Error Handling:

Error handling is implemented for fetching currency codes and exchange rates from the API.
If there's an error, it is printed to the console, and appropriate actions are taken to handle the error gracefully.
Application Lifecycle:


Upon closing the window, the background thread is stopped, and the application exits gracefully.
The script is well-structured, with clear separation of concerns between GUI creation, data fetching, and currency conversion functionalities. It provides a simple and intuitive interface for users to convert currencies, along with error handling and background updating of exchange rates for a seamless experience.

Image of an App:

![converter app](https://github.com/ganeshnaik10/CurrencyConverter/assets/114274628/7382bfde-c53b-49d1-93da-06cd82c32dee)

