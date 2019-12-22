clean:
	@rm -f data/images/*.png
	@rm -f ml/images/glassy/*.png ml/images/choppy/*.png

compress-data:
	@tar -czf data/images/images.tar.gz data/images/*.png
	@tar -czf ml/images/images.tar.gz ml/images/glassy/*.png ml/images/choppy/*.png 

decompress-data:
	@tar -xzf data/images/images.tar.gz
	@tar -xzf ml/images/images.tar.gz

.PHONY: clean compress-data decompress-data
