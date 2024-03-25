SELECT
  time,
  blob_submitter,
  SUM(blobs) AS TotalBlobs,
  SUM(eth_fees) AS TotalEthFees,
  SUM(usd_fees) AS TotalUSDFees
FROM
  dune.jessica99al.dataset_query_result55
GROUP BY
  time, blob_submitter
ORDER BY
  time, blob_submitter;
