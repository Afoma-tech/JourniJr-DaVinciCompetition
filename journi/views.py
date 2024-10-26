from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from .forms import kidregform
import openai
import os

# Create your views here.
openai.api_key = os.getenv('OPENAI_API_KEY')

def homepage(request):
    return render(request, 'index.html')

# def kidregpage(request):
#    form = kidregform()
#    return render(request, 'kid_registration.html', {'form': form})

def kidregpage(request):
    form = kidregform()
    if request.method == 'POST':
        form = kidregform(request.POST)
        if form.is_valid():
            form.save()

            return redirect('dashpage')
        else:
            # Print form errors to the console if validation fails
            print("Form errors:", form.errors)

    return render(request, 'kid_registration.html', {'form': form})

def travelpack(request):
    return render(request, 'travelkit1.html')

def dashpage(request):
    return render(request, 'dashboard.html')

def loginpage(request):
    if request.method == 'POST':
        return redirect('kid_registration.html')

    return render(request, 'login.html')

def food_view(request):
    return render(request, 'food.html')

def generate_packaging_kit(request):
    # Example user profile data
    registration_data = {
        "user": {
            "name": "Alex",
            "age": 21,
            "gender": "male",
            "allergies": None
        },
        "travel_party": [
            {
                "name": "Anna",
                "relationship": "wife",
                "age": 21,
                "allergies": "peanut"
            },
            {
                "name": "Katie",
                "relationship": "daughter",
                "age": 1.5,
                "allergies": "fish",
                "special_needs": "baby supplies"
            }
        ],
        "destination": {
            "city": "Paris",
            "country": "France"
        },
        "preferences": {
            "sightseeing": True,
            "dietary": "based on allergies"
        }
    }

    try:
        # Prepare the prompt for GPT
        prompt = (
            "Create a packaging kit based on the following user profile:\n"
            f"**User Information:**\n"
            f"- Name: {registration_data['user']['name']}\n"
            f"- Age: {registration_data['user']['age']}\n"
            f"- Gender: {registration_data['user']['gender']}\n"
            f"- Allergies: {registration_data['user']['allergies']}\n\n"
            "**Travel Party:**\n"
        )

        for member in registration_data['travel_party']:
            prompt += (
                f"- Name: {member['name']}, Relationship: {member['relationship']}, "
                f"Age: {member['age']}, Allergies: {member.get('allergies', 'None')}\n"
            )

        prompt += (
            f"\n**Destination:**\n"
            f"- City: {registration_data['destination']['city']}, "
            f"Country: {registration_data['destination']['country']}\n\n"
            f"**Preferences:**\n"
            f"- Sightseeing: {registration_data['preferences']['sightseeing']}\n"
            f"- Dietary Preferences: {registration_data['preferences']['dietary']}\n\n"
            "Organize the output under sections such as 'Packing List', 'Food Recommendations', and 'Sightseeing'."
        )

        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a packaging expert. Help users create the best packaging kit based on their profiles."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.8
        )

        # Extract the content safely from the response
        kit = response.choices[0].message.content.strip() if response.choices else "No content generated."

        # Store the generated kit in session (optional)
        request.session['packaging_kit'] = kit

        # Render the kit on the kit.html template
        return render(request, 'kit.html', {'kit': kit})

    except Exception as e:
        # Print and return an error if kit generation fails
        print(f"Error creating packaging kit: {e}")
        return HttpResponseBadRequest("Failed to generate packaging kit.")

def chat_with_bot(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            try:
                # Send the user message to OpenAI
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant. Answer the user's questions and assist them."
                        },
                        {
                            "role": "user",
                            "content": user_message,
                        }
                    ],
                    temperature=0.7
                )

                # Get the bot's response
                bot_response = response.choices[0].message.content.strip()

                # Return the response as JSON
                return JsonResponse({'response': bot_response})

            except Exception as e:
                print(f"Error in chat with bot: {e}")
                return JsonResponse({'response': "Sorry, I couldn't process your request."})
        else:
            return JsonResponse({'response': "No message received."})
    return HttpResponseBadRequest("Invalid request.")


def doctor_view(request):
    return render(request, 'doctor.html')