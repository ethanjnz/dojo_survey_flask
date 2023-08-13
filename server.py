from flask import Flask, render_template, redirect, request, session
import flask_app.controllers.surveys
from flask_app import app

if __name__ == "__main__":
    app.run(debug=True)
