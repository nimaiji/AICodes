# :tree: Decision Tree and Random Forest Classifier

This Python script employs the scikit-learn library to implement a Decision Tree Classifier and a Random Forest Classifier for the analysis of a Twitter dataset containing real and fake tweets. The script covers the following aspects:

## Author
- **Nima Iji**
- **Email:** ijinima@gmail.com

## Dataset
The script utilizes two CSV files, 'pol-real.csv' and 'pol-fake.csv', representing real and fake tweets, respectively. The dataset is merged and randomly sampled to ensure balanced representation.

## Decision Tree Classification
### Gini Criterion
- The script first builds a Decision Tree using the default Gini criterion.
- Confusion matrix, classification report, and balanced accuracy score are generated and printed.
- The resulting Decision Tree is visualized and saved as 'Gini.png'.

### Information Gain Criterion
- The script then constructs a Decision Tree using the Information Gain criterion (entropy).
- Similar evaluation metrics are generated and printed.
- The resulting Decision Tree is visualized and saved as 'InformationGain.png'.

## 10-Fold Cross-Validation
- The script performs 10-Fold Cross-Validation to find the optimal maximum depth for the Decision Tree.
- The accuracy for each depth is printed, and the best accuracy is displayed.

## Random Forest Classification
- The script employs a Random Forest Classifier with 20 estimators.
- The balanced accuracy score is printed.

## Usage
1. Ensure you have the required libraries installed: `matplotlib`, `pandas`, and `scikit-learn`.
2. Provide the 'pol-real.csv' and 'pol-fake.csv' files in the same directory as the script.
3. Run the script using a Python interpreter.

## Note
- Uncommented lines related to saving datasets and figures can be uncommented as needed for further analysis and documentation.

Feel free to explore and modify the script for your specific use case. Happy coding!
