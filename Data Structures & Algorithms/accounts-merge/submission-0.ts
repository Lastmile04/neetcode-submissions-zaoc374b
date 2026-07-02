class Solution {
    /**
     * @param {string[][]} accounts
     * @return {string[][]}
     */
    accountsMerge(accounts: string[][]): string[][] {
        const emailToName: Map<string, string> = new Map();
        const adjList: Map<string, string[]> = new Map();

        for (let account of accounts) {
            const name = account[0];
            const firstEmail = account[1];

            for (let i = 1; i < account.length; i++) {
                const currentEmail = account[i];

                emailToName.set(currentEmail, name);

                if (!adjList.has(currentEmail)) adjList.set(currentEmail, []);
                if (!adjList.has(firstEmail)) adjList.set(firstEmail, []);

                if (currentEmail !== firstEmail) {
                    adjList.get(currentEmail)!.push(firstEmail);
                    adjList.get(firstEmail)!.push(currentEmail);
                }
            }
        }

        const visited: Set<string> = new Set();
        const mergedAccounts: string[][] = [];
        // dfs traversal funciton 
        const dfs = (email: string, component: string[]) => {
            visited.add(email);
            component.push(email);

            const neighbours = adjList.get(email)!;
            for (const nei of neighbours) {
                if (!visited.has(nei)) dfs(nei, component);
            }
        }

        for (const email of adjList.keys()) {
            if (!visited.has(email)) {
                const component: string[] = [];
                dfs(email, component);

                component.sort();

                const name = emailToName.get(email)!;
                mergedAccounts.push([name, ...component]);
            }
        }

        return mergedAccounts;
    }
}

