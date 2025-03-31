from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

def create_color_array():
    color_list = []
    color_list.append("Megan's Favorirte Color is Pink")
    color_list.append("Adriana's Favorirte Color is Red")
    return color_list

preset_colors = create_color_array()

@app.route('/', methods=['GET', 'POST']) 
def colors():
    if request.method == 'POST':
        name = request.form.get('name')
        color = request.form.get('color')

        if name != "" and color !="":
            return redirect(url_for('your_color', name=name, color=color))
        
        return "ITS EMPTY!" 

    return """
    <h1>What's your favorite color? Add your Favorite to the List! </h1>
    <form method="post">
        Name: <input type="text" name="name"><br>
        Favorite Color: <input type="text" name="color"><br>
        <input type="submit" value="LETS GO">
    </form> 
    """

@app.route('/your_color') 
def your_color():
    query_name = request.args.get('name')
    query_color = request.args.get('color')
    preset_colors.append(f"{query_name}'s Favorirte Color is {query_color}")

    return f"""
    <h2> Hi {query_name}! {query_color} is a cool color!</h2>
    <br></br>
    <a href="/all_colors">See Everyone's Favorite Colors :)</a>
    """
  
@app.route('/all_colors') 
def all_colors():
    color_list_html = "".join([f"<h2>{color}</h2>" for color in preset_colors])
    return f"""
    <h1>Here's Everyone's Favorite Colors: </h1>
        <body>
            {color_list_html}
        </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


#SOURCES
#https://www.geeksforgeeks.org/what-is-cross-site-scripting-xss/
#https://www.geeksforgeeks.org/access-the-query-string-in-flask-routes/
#https://dulangirathnapala.medium.com/redirecting-to-another-page-with-button-click-in-python-flask-c112a2a2304c