# ClothingStoreAI

This project is a proof of concept (POC) designed to reduce the product registration bottleneck in a small clothing business. It combines Computer Vision, Large Language Models, and Machine Learning to generate product information and estimate a clothing item's selling price from a photo and its purchase price.

## The Problem

This project was inspired by a real operational challenge in a small family-owned clothing store.

Our business focuses on affordable clothing, with most products priced between **R$10 and R$50**. Since our strategy is based on high sales volume rather than high profit margins, products sell quickly and we restock every week.

Although we already use a management system, registering new products is still a manual process. For every new item, we need to:

- Write a product description
- Enter the purchase price
- Define the selling price

With hundreds of new items arriving every week, this process becomes repetitive, time-consuming, and creates a bottleneck in the inventory registration workflow.


## The Solution

This proof of concept was designed to reduce that bottleneck.

Instead of manually registering every product, the employee simply takes a photo of the clothing item using a mobile phone and enters its purchase price.

The image is first sent to a multimodal Large Language Model (LLM), which analyzes the product and extracts structured attributes.

Those extracted attributes are then sent in a second request to a LLM to generate a product description.

Finally, the structured attributes and the purchase price are used as input for a Machine Learning model trained on the store's pricing patterns to predict a suggested selling price.

By automating image analysis, product description generation, and price suggestion, the solution may significantly reduce the manual work required to register new products.

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

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- OpenAI API Key

### Configuration

Add your OpenAI API key in `appsettings.json` file and save it.

### Run

```bash
docker compose up --build -d
```
---
## Future Improvements

- Support uploading multiple images simultaneously.
- Allow users to review and edit the AI-generated product description before completing the registration.
- Eliminate the need to provide the purchase price by training the Machine Learning model to predict the selling price using only the clothing item's visual characteristics.
- Expand the solution to support additional use cases beyond product registration.

---
