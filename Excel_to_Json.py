import xlrd
import json
import os, fnmatch
import logging
#first you need to import xlrd and json module

# FILES_PATH = "/home/mesadmin/ucd-test-home/MedalliaLite/documents/test-cases"

# file = r'C:\Users\AlanManuelAcostaSala\MedalliaLite\documents\test-cases\Test_Negative_File_Medallia_Lite_2.xlsx' #name of the file you want to transform in json 
# fp = r'C:\Users\AlanManuelAcostaSala\MedalliaLite\documents\test-cases\Test_Negative_File_Medallia_Lite_2.json' #name of the json file you want to create

file = r'C:\Users\AlanManuelAcostaSala\test\Test_File_Medallia_Lite' + '.xlsx'
fp = r'C:\Users\AlanManuelAcostaSala\test\Test_File_Medallia_Lite' +  '.json'

fp = r'C:\Users\AlanManuelAcostaSala\Desktop\Test_File_Medallia_Lite.txt'

#This is the actual function that creates de json based on the excel

class MedalliaLiteAPI:
	INVITES_PATH = "/" + MedalliaLiteHandler.PostHandler.INVITES_PATH
	ORG_FILE_PATH = "/" + MedalliaLiteHandler.PostHandler.ORG_FILE_PATH
	SEND_INVITES_PATH = "/" + MedalliaLiteHandler.PostHandler.SEND_INVITES_PATH
	TEST_PAYLOAD_PATH = "/home/mesadmin/ucd-test-home/MedalliaLite/documents/test-cases"

	def submit_invites(config):
		logger.info("START - Medallia Lite Submit and Send Invites test.")
		medallia_lite_api = MedalliaLiteAPI(config['api-endpoint'])
		success = submit_invites_for_files(config, medallia_lite_api, medallia_lite_api.find_bu_test_files(), 404)
		logger.info("SUCCESS - Medallia Lite Submit and Send Invites test.")
		return success

	def get_invites(config, client_email, client_name, success_expected=True):
	    logger.info("START - Medallia Lite GET API test.")
	    medallia_lite_api = MedalliaLiteAPI(config['api-endpoint'])
	    result = medallia_lite_api.get_invites(config, client_email, client_name)
	    status = result['status']
	    data = result['data']
	    if status != 'success' and success_expected:
	        logger.error("GET returned unsuccessful status: " + status +  ", expecting success")
	        logger.error("Response data: " + json.dumps(data))
	        return False
	    logger.info("GET result data: " + json.dumps(data))
	    logger.info("SUCCESS - Medallia Lite GET API test.")
	    return True

def ImportarExcel(file,fp):
    data = []
    first_row = []
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_index(0)
    for col in range(worksheet.ncols):
        first_row.append( worksheet.cell_value(0,col))
    for row in range(1, worksheet.nrows):
        elm = {}
        for col in range(worksheet.ncols):
            elm[first_row[col]]=worksheet.cell_value(row,col)
        data.append(elm)
    json.dump(data, open(fp, 'w'))

def submit_invites_for_files(config, medallia_lite_api, test_input_files, response_code_expected):
	success = True
	for test_input_file in test_input_files:
		response = medallia_lite_api.submit_invites(config, test_input_file)
		result = response.json()
		status = result['status']
		data = result['data']
		if response.status_code != response_code_expected:
			logger.error("submit_invites_for_files saw response.status_code: " + response.status_code +  ", expecting: " + response.status_code)
			logger.error("Response data: " + json.dumps(data))
			success = False
			continue	# This test case failed, try the others but ultimate success will be false
		if response_code_expected == 404:
			logger.info("submit_invites_for_files saw response.status_code: " + response.status_code +  "as expected")
			continue	# This test case succeeded, e.g. we expected incorrect BU's, so we don't want to send the invites
		else:		# This test case succeeded and we do want to send the invites
			file_hash = data['file_hash']
			result = medallia_lite_api.send_invites(config, file_hash)
			status = result['status']
			data = result['data']
			if status != 'success':
				logger.error("submit_invites_for_files saw response.status_code: " + response.status_code +  ", expecting: " + response.status_code)
				logger.error("Response data: " + json.dumps(data))
				success = False

		logger.info("POST result data: " + json.dumps(data))

	return success

if __name__ == '__main__':
	ImportarExcel(file,fp)


# ImportarExcel(file,fp) #you call this function like this and you'll get your json

