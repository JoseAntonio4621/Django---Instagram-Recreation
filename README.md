{% extends "users/base.html" %}

{% block head_content %}
<title>Instagram | Sign in</title>
{% endblock %}



{% block container %}

    {% if error %}
        <p class="alert alert-danger">{{ error }}</p>
    {% endif%}
    
    <form method="POST" action="{% url "users:login" %}">
        {% csrf_token %}

        <div class="form-group">
            <input class="form-control" type="text" placeholder="Username" name="username" />
        </div>

        <div class="form-group">
            <input class="form-control" type="password" placeholder="Password" name="password" />
        </div>
        
        <button class="btn btn-primary btn-block mt-5" type="submit">Sign in!</button>

        <p>
            Don't have an account?
            <a href="{% url "users:signup" %}">Sign up!
                <i class="fas fa-sign-out-alt"></i>
            </a>
        </p>
        
    </form>
    

{% endblock %}
