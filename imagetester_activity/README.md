# ImageTester Activity - Test Images and PDFs
- Currently this is used in Paychex's TAF framework. We can also use it individually here. 
- [ImageTester Github](https://github.com/applitools/ImageTester)
### Prerequisites
1. [Install Java](https://www.oracle.com/java/technologies/downloads/)
2. Set your APPLITOOLS_SERVER_URL environment variable to https://service-outbound-par.paychex.com/pxt-applitools. 
3. Set your APPLITOOLS_API_KEY environment variable. 
4. Download the [Imagetester jar file](https://github.com/applitools/ImageTester/releases/tag/2.3.7)

### Activity
1. Find a pdf or image file to test.
2. Run Imagetester: 
``` 
java -jar ImageTester_2.3.7.jar -fp your/file/path/imagename.extension
```
3. You should see the image being tested on the Applitools dashboard. Try a longer PDF document. 
4. Explore the different run options available from the imagetester github repo.   
