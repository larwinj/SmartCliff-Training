const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

function findMedianSortedArrays(nums1, nums2) {
    const merged = [...nums1, ...nums2].sort((a, b) => a - b);
    const n = merged.length;

    if (n % 2 === 0) {
        return (merged[n / 2 - 1] + merged[n / 2]) / 2.0;
    } else {
        return merged[Math.floor(n / 2)];
    }
}

async function main() {
    let arr1 = await crw.get("Enter first sorted array (comma separated): ");
    let arr2 = await crw.get("Enter second sorted array (comma separated): ");

    arr1 = arr1.split(",").map(Number);
    arr2 = arr2.split(",").map(Number);

    const median = findMedianSortedArrays(arr1, arr2);
    console.log("Median:", median);

    crw.close();
}

main();
