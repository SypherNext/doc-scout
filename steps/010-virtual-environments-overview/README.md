# Step 010: Virtual Environments

AI projects have notoriously complex dependency trees. Your project needs `numpy==1.26.0`, another needs `numpy==1.24.3`, and your system Python cannot hold both versions simultaneously in the same site-packages directory. Without isolation, you face version conflicts that manifest as cryptic errors, or worse, silent behavioural differences that produce wrong results. Virtual environments solve this by giving each...

This lesson is conceptual (an overview or a review) and introduces no new runnable scripts of its own; see the Hands-On and Common Mistakes steps around it for code.
