from PyPDF2 import PdfReader
from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Create your views here.

from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def index(request):
    if 'pdf_content' in request.session:
        pdf_content = request.session['pdf_content']
        # pdf_file_path = r'D:\Code\Research\CDE\Django\UI\static\Jay_Resume.pdf'
    else:
        pdf_content = None

    return render(request, 'index.html', {'pdf_content': pdf_content})


def upload_pdf(request):
    if request.method == 'POST' and 'pdf_file' in request.FILES:
        pdf_file = request.FILES['pdf_file']
        pdf_content = extract_pdf_content(pdf_file)
        request.session['pdf_content'] = pdf_content

        return redirect('index')
    return redirect('home')


def extract_pdf_content(pdf_file):
    # Extract PDF content
    pdf_reader = PdfReader(pdf_file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text


def chats(request):
    return render(request, 'chats.html')
