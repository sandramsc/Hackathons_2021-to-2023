'use client';

import React, { useState, useEffect } from 'react';

export default function ClientRehydration({ children }: { children: React.ReactNode }) {
    const [hasMounted, setHasMounted] = useState(false);

    useEffect(() => {
        setHasMounted(true);
    }, [])

    if (!hasMounted) return null;

    return (
        <div>
            {children}
        </div>
    );
};