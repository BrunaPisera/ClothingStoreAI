# ClothingStoreAI

An end-to-end proof of concept that combines Computer Vision, Large Language Models, and Machine Learning to estimate the selling price of clothing items from a photo and their purchase cost.

```text
React
   │
   ▼
ASP.NET API
   │
   ├── OpenAI Vision
   │
   └── Python ML Model
           │
           ▼
     Predicted Price
```
---

## The Problem

In many small clothing stores, pricing is based not only on the purchase cost but also on the product's visual characteristics and perceived value.

Attributes such as:

- Clothing category
- Sleeve type
- Premium appearance

can all influence the final selling price.

To project uses a multimodal Large Language Model (LLM) to analyze the clothing image, extract structured attributes, and provide the information required by a Machine Learning model to predict a selling price.

---

## Technologies

### Backend

- ASP.NET
- C#
- OpenAI API

### Frontend

- React
- TypeScript

### Machine Learning

- Python
- Pandas
- Scikit-learn
- Joblib

---

## Solution Architecture

<img width="421" height="800" alt="Diagrama sem nome drawio (3)" src="https://github.com/user-attachments/assets/12b1ad6a-e54e-4be7-b375-7fb75c9fa883" />


The prediction pipeline follows these steps:

1. The user uploads a clothing image and provides its purchase cost.
2. The .NET API sends the image to the OpenAI Vision model.
3. The model extracts structured clothing attributes in JSON format.
4. Those attributes are converted into a textual description.
5. The description and structured data are transformed into features.
6. A trained Machine Learning model predicts the suggested selling price.
7. The React application displays the predicted price together with the generated description.

---

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- OpenAI API Key

### Configuration

Add your OpenAI API key in `appsettings.json` file and save it.

### Run

```bash
docker compose up --build
```
---
## Future Improvements

- Replace the synthetic dataset with real sales data.
- Improve feature extraction.
- Fine-tune prompts for greater consistency.
- Deploy the solution to the cloud.
- Support batch image processing.

---
