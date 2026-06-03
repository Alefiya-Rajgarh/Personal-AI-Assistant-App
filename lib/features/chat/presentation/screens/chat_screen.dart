import 'package:flutter/material.dart';

import '../../../../core/widgets/aegis_empty_state.dart';

class ChatScreen extends StatelessWidget {
  const ChatScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Chat concierge')),
      body: const AegisEmptyState(
        icon: Icons.chat_bubble_outline,
        title: 'No conversations yet',
        subtitle: 'Start a conversation to brief your AI executive assistant.',
      ),
    );
  }
}
