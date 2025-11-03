import React, { useState } from "react";
import {
  ChakraProvider, Box, Button, Input, Checkbox, Spinner,
  Text, VStack, HStack, Textarea, Select
} from "@chakra-ui/react";
import { startScrape, getStatus, getResults, downloadFile, scoreText, deaiText } from "./api";

function App() {
  const [url, setUrl] = useState("");
  const [docTypes, setDocTypes] = useState(["docx", "pdf", "csv", "xlsx", "pptx", "txt"]);
  const [jobId, setJobId] = useState(null);
  const [status, setStatus] = useState("");
  const [progress, setProgress] = useState(0);
  const [results, setResults] = useState([]);
  const [domain, setDomain] = useState("");
  const [error, setError] = useState("");

  const [scoreTextInput, setScoreTextInput] = useState("");
  const [scoreResult, setScoreResult] = useState(null);
  const [deaiTextInput, setDeaiTextInput] = useState("");
  const [deaiLevel, setDeaiLevel] = useState(1);
  const [deaiResult, setDeaiResult] = useState("");
  
  const handleStart = async () => {
    setError("");
    try {
      let res = await startScrape(url, docTypes);
      setJobId(res.job_id);
      setDomain(new URL(url).hostname);
      setStatus("running");
      setProgress(0);
      setResults([]);
    } catch (err) {
      setError("Failed to start scrape. Check your URL and server.");
    }
  };
  const handleCheckStatus = async () => {
    setError("");
    if (!jobId) return;
    try {
      let res = await getStatus(jobId);
      setStatus(res.status);
      setProgress(res.progress);
      if (res.status === "done") {
        let files = await getResults(domain);
        setResults(files.files);
      }
    } catch (err) {
      setError("Failed to check status. Is the server running?");
    }
  };
  const handleScoreText = async () => {
    setError("");
    try {
      let res = await scoreText(scoreTextInput);
      setScoreResult(res);
    } catch (err) {
      setError("Failed to score text.");
    }
  };
  const handleDeaiText = async () => {
    setError("");
    try {
      let res = await deaiText(deaiTextInput, deaiLevel);
      setDeaiResult(res.deai_text);
    } catch (err) {
      setError("Failed to De-AI text.");
    }
  };
  
  return (
    <ChakraProvider>
      <Box maxW="900px" mx="auto" py="10">
        <Text fontSize="3xl" fontWeight="bold" mb="3" color="blue.700">
          Universal Educational Web Scraper & AI Text Analyzer
        </Text>
        {error && (
          <Box p={3} mb={5} borderRadius="md" bg="red.100">
            <Text color="red.700">{error}</Text>
          </Box>
        )}
        {/* Scraper UI */}
        <Box boxShadow="md" p={5} mb={8} borderRadius="xl" bg="gray.50">
          <Text fontSize="lg" fontWeight="bold" mb={2}>Website/Document Scraper</Text>
          <VStack spacing={4} align="stretch">
            <Input placeholder="Enter website URL" value={url} onChange={e => setUrl(e.target.value)} />
            <HStack>
              {["docx", "pdf", "csv", "xlsx", "pptx", "txt"].map(type => (
                <Checkbox key={type} isChecked={docTypes.includes(type)} onChange={e => {
                  if (e.target.checked) setDocTypes([...docTypes, type]);
                  else setDocTypes(docTypes.filter(t => t !== type));
                }}>{type.toUpperCase()}</Checkbox>
              ))}
            </HStack>
            <Button colorScheme="blue" onClick={handleStart}>Start Scrape</Button>
            <Button colorScheme="green" onClick={handleCheckStatus} isDisabled={!jobId}>Check Status</Button>
            {status && <Text>Status: {status} | Progress: {progress}%</Text>}
            {status === "running" && <Spinner />}
            {results.length > 0 && (
              <Box mt="5">
                <Text fontWeight="bold">Results for {domain}:</Text>
                <VStack>
                  {results.map(file => (
                    <Button key={file} onClick={() => downloadFile(domain, file)}>{file}</Button>
                  ))}
                </VStack>
              </Box>
            )}
          </VStack>
        </Box>
        {/* AI Text Scoring UI */}
        <Box boxShadow="md" p={5} mb={8} borderRadius="xl" bg="gray.50">
          <Text fontSize="lg" fontWeight="bold" mb={2}>AI Text Scoring</Text>
          <Textarea
            placeholder="Paste text here to score"
            value={scoreTextInput}
            onChange={e => setScoreTextInput(e.target.value)}
            mb={2}
            rows={6}
          />
          <Button colorScheme="purple" onClick={handleScoreText}>Score Text</Button>
          {scoreResult && (
            <Box mt={3} p={3} borderRadius="md" bg="purple.100">
              <Text>Score: <b>{scoreResult.score}</b> / 100</Text>
              <Text>{scoreResult.label}</Text>
            </Box>
          )}
        </Box>
        {/* De-AI UI */}
        <Box boxShadow="md" p={5} mb={8} borderRadius="xl" bg="gray.50">
          <Text fontSize="lg" fontWeight="bold" mb={2}>De-AI Text (Humanize)</Text>
          <Textarea
            placeholder="Paste AI-generated or formal text here"
            value={deaiTextInput}
            onChange={e => setDeaiTextInput(e.target.value)}
            mb={2}
            rows={6}
          />
          <Select value={deaiLevel} onChange={e => setDeaiLevel(Number(e.target.value))} mb={2}>
            <option value={1}>Level 1 - Mild Humanization</option>
            <option value={2}>Level 2 - Conversational</option>
            <option value={3}>Level 3 - Narrative, Mistakes, Informal</option>
          </Select>
          <Button colorScheme="orange" onClick={handleDeaiText}>De-AI Text</Button>
          {deaiResult && (
            <Box mt={3} p={3} borderRadius="md" bg="orange.100">
              <Text>De-AI'd Text:</Text>
              <Textarea value={deaiResult} readOnly rows={8} />
            </Box>
          )}
        </Box>
      </Box>
    </ChakraProvider>
  );
}

export default App;